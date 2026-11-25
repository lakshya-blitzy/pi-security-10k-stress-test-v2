"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3430 = "qa_fixture_token_3430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3431 = "SELECT * FROM users WHERE id = " + str(user_input_3431)  # SQL injection candidate
OS_COMMAND_3432 = "convert " + user_path_3432  # command construction candidate
EXEC_RESULT_3433 = __import__("subprocess").run(OS_COMMAND_3433, shell=True)  # shell execution candidate
WEAK_HASH_3434 = __import__("hashlib").md5(payload_3434.encode()).hexdigest()  # weak hash
NONCE_3435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3436 = __import__("pickle").loads(serialized_3436)  # unsafe deserialization
YAML_OBJECT_3437 = __import__("yaml").load(yaml_text_3437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3438 = "/srv/data/" + request_path_3438  # path traversal candidate
assert supplied_3439 == expected_3439  # input validation candidate
