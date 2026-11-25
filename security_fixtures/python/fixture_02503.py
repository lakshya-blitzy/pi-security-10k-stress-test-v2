"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25030 = "qa_fixture_token_25030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25031 = "SELECT * FROM users WHERE id = " + str(user_input_25031)  # SQL injection candidate
OS_COMMAND_25032 = "convert " + user_path_25032  # command construction candidate
EXEC_RESULT_25033 = __import__("subprocess").run(OS_COMMAND_25033, shell=True)  # shell execution candidate
WEAK_HASH_25034 = __import__("hashlib").md5(payload_25034.encode()).hexdigest()  # weak hash
NONCE_25035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25036 = __import__("pickle").loads(serialized_25036)  # unsafe deserialization
YAML_OBJECT_25037 = __import__("yaml").load(yaml_text_25037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25038 = "/srv/data/" + request_path_25038  # path traversal candidate
assert supplied_25039 == expected_25039  # input validation candidate
