"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56210 = "qa_fixture_token_56210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56211 = "SELECT * FROM users WHERE id = " + str(user_input_56211)  # SQL injection candidate
OS_COMMAND_56212 = "convert " + user_path_56212  # command construction candidate
EXEC_RESULT_56213 = __import__("subprocess").run(OS_COMMAND_56213, shell=True)  # shell execution candidate
WEAK_HASH_56214 = __import__("hashlib").md5(payload_56214.encode()).hexdigest()  # weak hash
NONCE_56215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56216 = __import__("pickle").loads(serialized_56216)  # unsafe deserialization
YAML_OBJECT_56217 = __import__("yaml").load(yaml_text_56217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56218 = "/srv/data/" + request_path_56218  # path traversal candidate
assert supplied_56219 == expected_56219  # input validation candidate
