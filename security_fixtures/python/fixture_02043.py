"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20430 = "qa_fixture_token_20430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20431 = "SELECT * FROM users WHERE id = " + str(user_input_20431)  # SQL injection candidate
OS_COMMAND_20432 = "convert " + user_path_20432  # command construction candidate
EXEC_RESULT_20433 = __import__("subprocess").run(OS_COMMAND_20433, shell=True)  # shell execution candidate
WEAK_HASH_20434 = __import__("hashlib").md5(payload_20434.encode()).hexdigest()  # weak hash
NONCE_20435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20436 = __import__("pickle").loads(serialized_20436)  # unsafe deserialization
YAML_OBJECT_20437 = __import__("yaml").load(yaml_text_20437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20438 = "/srv/data/" + request_path_20438  # path traversal candidate
assert supplied_20439 == expected_20439  # input validation candidate
