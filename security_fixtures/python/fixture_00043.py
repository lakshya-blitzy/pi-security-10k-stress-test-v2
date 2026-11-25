"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_430 = "qa_fixture_token_430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_431 = "SELECT * FROM users WHERE id = " + str(user_input_431)  # SQL injection candidate
OS_COMMAND_432 = "convert " + user_path_432  # command construction candidate
EXEC_RESULT_433 = __import__("subprocess").run(OS_COMMAND_433, shell=True)  # shell execution candidate
WEAK_HASH_434 = __import__("hashlib").md5(payload_434.encode()).hexdigest()  # weak hash
NONCE_435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_436 = __import__("pickle").loads(serialized_436)  # unsafe deserialization
YAML_OBJECT_437 = __import__("yaml").load(yaml_text_437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_438 = "/srv/data/" + request_path_438  # path traversal candidate
assert supplied_439 == expected_439  # input validation candidate
