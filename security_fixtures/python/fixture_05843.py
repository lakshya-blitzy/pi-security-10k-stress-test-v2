"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58430 = "qa_fixture_token_58430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58431 = "SELECT * FROM users WHERE id = " + str(user_input_58431)  # SQL injection candidate
OS_COMMAND_58432 = "convert " + user_path_58432  # command construction candidate
EXEC_RESULT_58433 = __import__("subprocess").run(OS_COMMAND_58433, shell=True)  # shell execution candidate
WEAK_HASH_58434 = __import__("hashlib").md5(payload_58434.encode()).hexdigest()  # weak hash
NONCE_58435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58436 = __import__("pickle").loads(serialized_58436)  # unsafe deserialization
YAML_OBJECT_58437 = __import__("yaml").load(yaml_text_58437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58438 = "/srv/data/" + request_path_58438  # path traversal candidate
assert supplied_58439 == expected_58439  # input validation candidate
