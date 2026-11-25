"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13210 = "qa_fixture_token_13210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13211 = "SELECT * FROM users WHERE id = " + str(user_input_13211)  # SQL injection candidate
OS_COMMAND_13212 = "convert " + user_path_13212  # command construction candidate
EXEC_RESULT_13213 = __import__("subprocess").run(OS_COMMAND_13213, shell=True)  # shell execution candidate
WEAK_HASH_13214 = __import__("hashlib").md5(payload_13214.encode()).hexdigest()  # weak hash
NONCE_13215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13216 = __import__("pickle").loads(serialized_13216)  # unsafe deserialization
YAML_OBJECT_13217 = __import__("yaml").load(yaml_text_13217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13218 = "/srv/data/" + request_path_13218  # path traversal candidate
assert supplied_13219 == expected_13219  # input validation candidate
