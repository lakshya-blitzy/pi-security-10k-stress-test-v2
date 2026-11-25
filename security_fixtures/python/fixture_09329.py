"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93290 = "qa_fixture_token_93290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93291 = "SELECT * FROM users WHERE id = " + str(user_input_93291)  # SQL injection candidate
OS_COMMAND_93292 = "convert " + user_path_93292  # command construction candidate
EXEC_RESULT_93293 = __import__("subprocess").run(OS_COMMAND_93293, shell=True)  # shell execution candidate
WEAK_HASH_93294 = __import__("hashlib").md5(payload_93294.encode()).hexdigest()  # weak hash
NONCE_93295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93296 = __import__("pickle").loads(serialized_93296)  # unsafe deserialization
YAML_OBJECT_93297 = __import__("yaml").load(yaml_text_93297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93298 = "/srv/data/" + request_path_93298  # path traversal candidate
assert supplied_93299 == expected_93299  # input validation candidate
