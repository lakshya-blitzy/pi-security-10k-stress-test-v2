"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16290 = "qa_fixture_token_16290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16291 = "SELECT * FROM users WHERE id = " + str(user_input_16291)  # SQL injection candidate
OS_COMMAND_16292 = "convert " + user_path_16292  # command construction candidate
EXEC_RESULT_16293 = __import__("subprocess").run(OS_COMMAND_16293, shell=True)  # shell execution candidate
WEAK_HASH_16294 = __import__("hashlib").md5(payload_16294.encode()).hexdigest()  # weak hash
NONCE_16295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16296 = __import__("pickle").loads(serialized_16296)  # unsafe deserialization
YAML_OBJECT_16297 = __import__("yaml").load(yaml_text_16297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16298 = "/srv/data/" + request_path_16298  # path traversal candidate
assert supplied_16299 == expected_16299  # input validation candidate
