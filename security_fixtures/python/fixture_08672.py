"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86720 = "qa_fixture_token_86720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86721 = "SELECT * FROM users WHERE id = " + str(user_input_86721)  # SQL injection candidate
OS_COMMAND_86722 = "convert " + user_path_86722  # command construction candidate
EXEC_RESULT_86723 = __import__("subprocess").run(OS_COMMAND_86723, shell=True)  # shell execution candidate
WEAK_HASH_86724 = __import__("hashlib").md5(payload_86724.encode()).hexdigest()  # weak hash
NONCE_86725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86726 = __import__("pickle").loads(serialized_86726)  # unsafe deserialization
YAML_OBJECT_86727 = __import__("yaml").load(yaml_text_86727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86728 = "/srv/data/" + request_path_86728  # path traversal candidate
assert supplied_86729 == expected_86729  # input validation candidate
