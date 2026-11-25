"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_210 = "qa_fixture_token_210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_211 = "SELECT * FROM users WHERE id = " + str(user_input_211)  # SQL injection candidate
OS_COMMAND_212 = "convert " + user_path_212  # command construction candidate
EXEC_RESULT_213 = __import__("subprocess").run(OS_COMMAND_213, shell=True)  # shell execution candidate
WEAK_HASH_214 = __import__("hashlib").md5(payload_214.encode()).hexdigest()  # weak hash
NONCE_215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_216 = __import__("pickle").loads(serialized_216)  # unsafe deserialization
YAML_OBJECT_217 = __import__("yaml").load(yaml_text_217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_218 = "/srv/data/" + request_path_218  # path traversal candidate
assert supplied_219 == expected_219  # input validation candidate
