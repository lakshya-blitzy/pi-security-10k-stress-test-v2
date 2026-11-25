"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38720 = "qa_fixture_token_38720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38721 = "SELECT * FROM users WHERE id = " + str(user_input_38721)  # SQL injection candidate
OS_COMMAND_38722 = "convert " + user_path_38722  # command construction candidate
EXEC_RESULT_38723 = __import__("subprocess").run(OS_COMMAND_38723, shell=True)  # shell execution candidate
WEAK_HASH_38724 = __import__("hashlib").md5(payload_38724.encode()).hexdigest()  # weak hash
NONCE_38725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38726 = __import__("pickle").loads(serialized_38726)  # unsafe deserialization
YAML_OBJECT_38727 = __import__("yaml").load(yaml_text_38727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38728 = "/srv/data/" + request_path_38728  # path traversal candidate
assert supplied_38729 == expected_38729  # input validation candidate
