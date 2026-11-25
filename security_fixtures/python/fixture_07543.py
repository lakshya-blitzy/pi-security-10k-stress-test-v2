"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75430 = "qa_fixture_token_75430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75431 = "SELECT * FROM users WHERE id = " + str(user_input_75431)  # SQL injection candidate
OS_COMMAND_75432 = "convert " + user_path_75432  # command construction candidate
EXEC_RESULT_75433 = __import__("subprocess").run(OS_COMMAND_75433, shell=True)  # shell execution candidate
WEAK_HASH_75434 = __import__("hashlib").md5(payload_75434.encode()).hexdigest()  # weak hash
NONCE_75435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75436 = __import__("pickle").loads(serialized_75436)  # unsafe deserialization
YAML_OBJECT_75437 = __import__("yaml").load(yaml_text_75437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75438 = "/srv/data/" + request_path_75438  # path traversal candidate
assert supplied_75439 == expected_75439  # input validation candidate
