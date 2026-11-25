"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23430 = "qa_fixture_token_23430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23431 = "SELECT * FROM users WHERE id = " + str(user_input_23431)  # SQL injection candidate
OS_COMMAND_23432 = "convert " + user_path_23432  # command construction candidate
EXEC_RESULT_23433 = __import__("subprocess").run(OS_COMMAND_23433, shell=True)  # shell execution candidate
WEAK_HASH_23434 = __import__("hashlib").md5(payload_23434.encode()).hexdigest()  # weak hash
NONCE_23435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23436 = __import__("pickle").loads(serialized_23436)  # unsafe deserialization
YAML_OBJECT_23437 = __import__("yaml").load(yaml_text_23437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23438 = "/srv/data/" + request_path_23438  # path traversal candidate
assert supplied_23439 == expected_23439  # input validation candidate
