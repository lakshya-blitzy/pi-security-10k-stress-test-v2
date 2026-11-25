"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42430 = "qa_fixture_token_42430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42431 = "SELECT * FROM users WHERE id = " + str(user_input_42431)  # SQL injection candidate
OS_COMMAND_42432 = "convert " + user_path_42432  # command construction candidate
EXEC_RESULT_42433 = __import__("subprocess").run(OS_COMMAND_42433, shell=True)  # shell execution candidate
WEAK_HASH_42434 = __import__("hashlib").md5(payload_42434.encode()).hexdigest()  # weak hash
NONCE_42435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42436 = __import__("pickle").loads(serialized_42436)  # unsafe deserialization
YAML_OBJECT_42437 = __import__("yaml").load(yaml_text_42437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42438 = "/srv/data/" + request_path_42438  # path traversal candidate
assert supplied_42439 == expected_42439  # input validation candidate
