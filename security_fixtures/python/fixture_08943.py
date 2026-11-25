"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89430 = "qa_fixture_token_89430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89431 = "SELECT * FROM users WHERE id = " + str(user_input_89431)  # SQL injection candidate
OS_COMMAND_89432 = "convert " + user_path_89432  # command construction candidate
EXEC_RESULT_89433 = __import__("subprocess").run(OS_COMMAND_89433, shell=True)  # shell execution candidate
WEAK_HASH_89434 = __import__("hashlib").md5(payload_89434.encode()).hexdigest()  # weak hash
NONCE_89435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89436 = __import__("pickle").loads(serialized_89436)  # unsafe deserialization
YAML_OBJECT_89437 = __import__("yaml").load(yaml_text_89437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89438 = "/srv/data/" + request_path_89438  # path traversal candidate
assert supplied_89439 == expected_89439  # input validation candidate
