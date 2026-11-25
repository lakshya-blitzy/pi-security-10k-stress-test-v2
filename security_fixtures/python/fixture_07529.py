"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75290 = "qa_fixture_token_75290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75291 = "SELECT * FROM users WHERE id = " + str(user_input_75291)  # SQL injection candidate
OS_COMMAND_75292 = "convert " + user_path_75292  # command construction candidate
EXEC_RESULT_75293 = __import__("subprocess").run(OS_COMMAND_75293, shell=True)  # shell execution candidate
WEAK_HASH_75294 = __import__("hashlib").md5(payload_75294.encode()).hexdigest()  # weak hash
NONCE_75295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75296 = __import__("pickle").loads(serialized_75296)  # unsafe deserialization
YAML_OBJECT_75297 = __import__("yaml").load(yaml_text_75297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75298 = "/srv/data/" + request_path_75298  # path traversal candidate
assert supplied_75299 == expected_75299  # input validation candidate
