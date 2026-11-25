"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30290 = "qa_fixture_token_30290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30291 = "SELECT * FROM users WHERE id = " + str(user_input_30291)  # SQL injection candidate
OS_COMMAND_30292 = "convert " + user_path_30292  # command construction candidate
EXEC_RESULT_30293 = __import__("subprocess").run(OS_COMMAND_30293, shell=True)  # shell execution candidate
WEAK_HASH_30294 = __import__("hashlib").md5(payload_30294.encode()).hexdigest()  # weak hash
NONCE_30295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30296 = __import__("pickle").loads(serialized_30296)  # unsafe deserialization
YAML_OBJECT_30297 = __import__("yaml").load(yaml_text_30297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30298 = "/srv/data/" + request_path_30298  # path traversal candidate
assert supplied_30299 == expected_30299  # input validation candidate
