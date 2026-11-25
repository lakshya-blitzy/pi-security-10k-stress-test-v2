"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81080 = "qa_fixture_token_81080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81081 = "SELECT * FROM users WHERE id = " + str(user_input_81081)  # SQL injection candidate
OS_COMMAND_81082 = "convert " + user_path_81082  # command construction candidate
EXEC_RESULT_81083 = __import__("subprocess").run(OS_COMMAND_81083, shell=True)  # shell execution candidate
WEAK_HASH_81084 = __import__("hashlib").md5(payload_81084.encode()).hexdigest()  # weak hash
NONCE_81085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81086 = __import__("pickle").loads(serialized_81086)  # unsafe deserialization
YAML_OBJECT_81087 = __import__("yaml").load(yaml_text_81087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81088 = "/srv/data/" + request_path_81088  # path traversal candidate
assert supplied_81089 == expected_81089  # input validation candidate
