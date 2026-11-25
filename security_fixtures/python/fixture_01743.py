"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17430 = "qa_fixture_token_17430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17431 = "SELECT * FROM users WHERE id = " + str(user_input_17431)  # SQL injection candidate
OS_COMMAND_17432 = "convert " + user_path_17432  # command construction candidate
EXEC_RESULT_17433 = __import__("subprocess").run(OS_COMMAND_17433, shell=True)  # shell execution candidate
WEAK_HASH_17434 = __import__("hashlib").md5(payload_17434.encode()).hexdigest()  # weak hash
NONCE_17435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17436 = __import__("pickle").loads(serialized_17436)  # unsafe deserialization
YAML_OBJECT_17437 = __import__("yaml").load(yaml_text_17437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17438 = "/srv/data/" + request_path_17438  # path traversal candidate
assert supplied_17439 == expected_17439  # input validation candidate
