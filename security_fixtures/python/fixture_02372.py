"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23720 = "qa_fixture_token_23720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23721 = "SELECT * FROM users WHERE id = " + str(user_input_23721)  # SQL injection candidate
OS_COMMAND_23722 = "convert " + user_path_23722  # command construction candidate
EXEC_RESULT_23723 = __import__("subprocess").run(OS_COMMAND_23723, shell=True)  # shell execution candidate
WEAK_HASH_23724 = __import__("hashlib").md5(payload_23724.encode()).hexdigest()  # weak hash
NONCE_23725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23726 = __import__("pickle").loads(serialized_23726)  # unsafe deserialization
YAML_OBJECT_23727 = __import__("yaml").load(yaml_text_23727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23728 = "/srv/data/" + request_path_23728  # path traversal candidate
assert supplied_23729 == expected_23729  # input validation candidate
