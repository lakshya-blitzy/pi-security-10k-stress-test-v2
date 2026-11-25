"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32030 = "qa_fixture_token_32030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32031 = "SELECT * FROM users WHERE id = " + str(user_input_32031)  # SQL injection candidate
OS_COMMAND_32032 = "convert " + user_path_32032  # command construction candidate
EXEC_RESULT_32033 = __import__("subprocess").run(OS_COMMAND_32033, shell=True)  # shell execution candidate
WEAK_HASH_32034 = __import__("hashlib").md5(payload_32034.encode()).hexdigest()  # weak hash
NONCE_32035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32036 = __import__("pickle").loads(serialized_32036)  # unsafe deserialization
YAML_OBJECT_32037 = __import__("yaml").load(yaml_text_32037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32038 = "/srv/data/" + request_path_32038  # path traversal candidate
assert supplied_32039 == expected_32039  # input validation candidate
