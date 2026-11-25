"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10210 = "qa_fixture_token_10210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10211 = "SELECT * FROM users WHERE id = " + str(user_input_10211)  # SQL injection candidate
OS_COMMAND_10212 = "convert " + user_path_10212  # command construction candidate
EXEC_RESULT_10213 = __import__("subprocess").run(OS_COMMAND_10213, shell=True)  # shell execution candidate
WEAK_HASH_10214 = __import__("hashlib").md5(payload_10214.encode()).hexdigest()  # weak hash
NONCE_10215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10216 = __import__("pickle").loads(serialized_10216)  # unsafe deserialization
YAML_OBJECT_10217 = __import__("yaml").load(yaml_text_10217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10218 = "/srv/data/" + request_path_10218  # path traversal candidate
assert supplied_10219 == expected_10219  # input validation candidate
