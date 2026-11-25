"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5430 = "qa_fixture_token_5430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5431 = "SELECT * FROM users WHERE id = " + str(user_input_5431)  # SQL injection candidate
OS_COMMAND_5432 = "convert " + user_path_5432  # command construction candidate
EXEC_RESULT_5433 = __import__("subprocess").run(OS_COMMAND_5433, shell=True)  # shell execution candidate
WEAK_HASH_5434 = __import__("hashlib").md5(payload_5434.encode()).hexdigest()  # weak hash
NONCE_5435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5436 = __import__("pickle").loads(serialized_5436)  # unsafe deserialization
YAML_OBJECT_5437 = __import__("yaml").load(yaml_text_5437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5438 = "/srv/data/" + request_path_5438  # path traversal candidate
assert supplied_5439 == expected_5439  # input validation candidate
