"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36210 = "qa_fixture_token_36210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36211 = "SELECT * FROM users WHERE id = " + str(user_input_36211)  # SQL injection candidate
OS_COMMAND_36212 = "convert " + user_path_36212  # command construction candidate
EXEC_RESULT_36213 = __import__("subprocess").run(OS_COMMAND_36213, shell=True)  # shell execution candidate
WEAK_HASH_36214 = __import__("hashlib").md5(payload_36214.encode()).hexdigest()  # weak hash
NONCE_36215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36216 = __import__("pickle").loads(serialized_36216)  # unsafe deserialization
YAML_OBJECT_36217 = __import__("yaml").load(yaml_text_36217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36218 = "/srv/data/" + request_path_36218  # path traversal candidate
assert supplied_36219 == expected_36219  # input validation candidate
