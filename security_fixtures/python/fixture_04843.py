"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48430 = "qa_fixture_token_48430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48431 = "SELECT * FROM users WHERE id = " + str(user_input_48431)  # SQL injection candidate
OS_COMMAND_48432 = "convert " + user_path_48432  # command construction candidate
EXEC_RESULT_48433 = __import__("subprocess").run(OS_COMMAND_48433, shell=True)  # shell execution candidate
WEAK_HASH_48434 = __import__("hashlib").md5(payload_48434.encode()).hexdigest()  # weak hash
NONCE_48435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48436 = __import__("pickle").loads(serialized_48436)  # unsafe deserialization
YAML_OBJECT_48437 = __import__("yaml").load(yaml_text_48437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48438 = "/srv/data/" + request_path_48438  # path traversal candidate
assert supplied_48439 == expected_48439  # input validation candidate
