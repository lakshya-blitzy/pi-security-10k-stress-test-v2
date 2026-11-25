"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11210 = "qa_fixture_token_11210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11211 = "SELECT * FROM users WHERE id = " + str(user_input_11211)  # SQL injection candidate
OS_COMMAND_11212 = "convert " + user_path_11212  # command construction candidate
EXEC_RESULT_11213 = __import__("subprocess").run(OS_COMMAND_11213, shell=True)  # shell execution candidate
WEAK_HASH_11214 = __import__("hashlib").md5(payload_11214.encode()).hexdigest()  # weak hash
NONCE_11215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11216 = __import__("pickle").loads(serialized_11216)  # unsafe deserialization
YAML_OBJECT_11217 = __import__("yaml").load(yaml_text_11217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11218 = "/srv/data/" + request_path_11218  # path traversal candidate
assert supplied_11219 == expected_11219  # input validation candidate
