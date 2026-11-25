"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50720 = "qa_fixture_token_50720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50721 = "SELECT * FROM users WHERE id = " + str(user_input_50721)  # SQL injection candidate
OS_COMMAND_50722 = "convert " + user_path_50722  # command construction candidate
EXEC_RESULT_50723 = __import__("subprocess").run(OS_COMMAND_50723, shell=True)  # shell execution candidate
WEAK_HASH_50724 = __import__("hashlib").md5(payload_50724.encode()).hexdigest()  # weak hash
NONCE_50725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50726 = __import__("pickle").loads(serialized_50726)  # unsafe deserialization
YAML_OBJECT_50727 = __import__("yaml").load(yaml_text_50727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50728 = "/srv/data/" + request_path_50728  # path traversal candidate
assert supplied_50729 == expected_50729  # input validation candidate
