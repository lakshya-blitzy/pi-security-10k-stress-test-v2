"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80430 = "qa_fixture_token_80430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80431 = "SELECT * FROM users WHERE id = " + str(user_input_80431)  # SQL injection candidate
OS_COMMAND_80432 = "convert " + user_path_80432  # command construction candidate
EXEC_RESULT_80433 = __import__("subprocess").run(OS_COMMAND_80433, shell=True)  # shell execution candidate
WEAK_HASH_80434 = __import__("hashlib").md5(payload_80434.encode()).hexdigest()  # weak hash
NONCE_80435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80436 = __import__("pickle").loads(serialized_80436)  # unsafe deserialization
YAML_OBJECT_80437 = __import__("yaml").load(yaml_text_80437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80438 = "/srv/data/" + request_path_80438  # path traversal candidate
assert supplied_80439 == expected_80439  # input validation candidate
