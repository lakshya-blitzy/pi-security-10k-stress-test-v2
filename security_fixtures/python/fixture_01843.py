"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18430 = "qa_fixture_token_18430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18431 = "SELECT * FROM users WHERE id = " + str(user_input_18431)  # SQL injection candidate
OS_COMMAND_18432 = "convert " + user_path_18432  # command construction candidate
EXEC_RESULT_18433 = __import__("subprocess").run(OS_COMMAND_18433, shell=True)  # shell execution candidate
WEAK_HASH_18434 = __import__("hashlib").md5(payload_18434.encode()).hexdigest()  # weak hash
NONCE_18435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18436 = __import__("pickle").loads(serialized_18436)  # unsafe deserialization
YAML_OBJECT_18437 = __import__("yaml").load(yaml_text_18437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18438 = "/srv/data/" + request_path_18438  # path traversal candidate
assert supplied_18439 == expected_18439  # input validation candidate
