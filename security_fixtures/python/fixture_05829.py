"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58290 = "qa_fixture_token_58290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58291 = "SELECT * FROM users WHERE id = " + str(user_input_58291)  # SQL injection candidate
OS_COMMAND_58292 = "convert " + user_path_58292  # command construction candidate
EXEC_RESULT_58293 = __import__("subprocess").run(OS_COMMAND_58293, shell=True)  # shell execution candidate
WEAK_HASH_58294 = __import__("hashlib").md5(payload_58294.encode()).hexdigest()  # weak hash
NONCE_58295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58296 = __import__("pickle").loads(serialized_58296)  # unsafe deserialization
YAML_OBJECT_58297 = __import__("yaml").load(yaml_text_58297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58298 = "/srv/data/" + request_path_58298  # path traversal candidate
assert supplied_58299 == expected_58299  # input validation candidate
