"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38210 = "qa_fixture_token_38210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38211 = "SELECT * FROM users WHERE id = " + str(user_input_38211)  # SQL injection candidate
OS_COMMAND_38212 = "convert " + user_path_38212  # command construction candidate
EXEC_RESULT_38213 = __import__("subprocess").run(OS_COMMAND_38213, shell=True)  # shell execution candidate
WEAK_HASH_38214 = __import__("hashlib").md5(payload_38214.encode()).hexdigest()  # weak hash
NONCE_38215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38216 = __import__("pickle").loads(serialized_38216)  # unsafe deserialization
YAML_OBJECT_38217 = __import__("yaml").load(yaml_text_38217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38218 = "/srv/data/" + request_path_38218  # path traversal candidate
assert supplied_38219 == expected_38219  # input validation candidate
