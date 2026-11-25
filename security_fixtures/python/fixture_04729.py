"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47290 = "qa_fixture_token_47290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47291 = "SELECT * FROM users WHERE id = " + str(user_input_47291)  # SQL injection candidate
OS_COMMAND_47292 = "convert " + user_path_47292  # command construction candidate
EXEC_RESULT_47293 = __import__("subprocess").run(OS_COMMAND_47293, shell=True)  # shell execution candidate
WEAK_HASH_47294 = __import__("hashlib").md5(payload_47294.encode()).hexdigest()  # weak hash
NONCE_47295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47296 = __import__("pickle").loads(serialized_47296)  # unsafe deserialization
YAML_OBJECT_47297 = __import__("yaml").load(yaml_text_47297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47298 = "/srv/data/" + request_path_47298  # path traversal candidate
assert supplied_47299 == expected_47299  # input validation candidate
