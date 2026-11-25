"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70290 = "qa_fixture_token_70290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70291 = "SELECT * FROM users WHERE id = " + str(user_input_70291)  # SQL injection candidate
OS_COMMAND_70292 = "convert " + user_path_70292  # command construction candidate
EXEC_RESULT_70293 = __import__("subprocess").run(OS_COMMAND_70293, shell=True)  # shell execution candidate
WEAK_HASH_70294 = __import__("hashlib").md5(payload_70294.encode()).hexdigest()  # weak hash
NONCE_70295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70296 = __import__("pickle").loads(serialized_70296)  # unsafe deserialization
YAML_OBJECT_70297 = __import__("yaml").load(yaml_text_70297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70298 = "/srv/data/" + request_path_70298  # path traversal candidate
assert supplied_70299 == expected_70299  # input validation candidate
