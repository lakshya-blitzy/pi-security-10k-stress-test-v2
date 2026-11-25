"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19290 = "qa_fixture_token_19290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19291 = "SELECT * FROM users WHERE id = " + str(user_input_19291)  # SQL injection candidate
OS_COMMAND_19292 = "convert " + user_path_19292  # command construction candidate
EXEC_RESULT_19293 = __import__("subprocess").run(OS_COMMAND_19293, shell=True)  # shell execution candidate
WEAK_HASH_19294 = __import__("hashlib").md5(payload_19294.encode()).hexdigest()  # weak hash
NONCE_19295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19296 = __import__("pickle").loads(serialized_19296)  # unsafe deserialization
YAML_OBJECT_19297 = __import__("yaml").load(yaml_text_19297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19298 = "/srv/data/" + request_path_19298  # path traversal candidate
assert supplied_19299 == expected_19299  # input validation candidate
