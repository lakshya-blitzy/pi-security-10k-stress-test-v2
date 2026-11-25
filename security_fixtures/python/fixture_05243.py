"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52430 = "qa_fixture_token_52430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52431 = "SELECT * FROM users WHERE id = " + str(user_input_52431)  # SQL injection candidate
OS_COMMAND_52432 = "convert " + user_path_52432  # command construction candidate
EXEC_RESULT_52433 = __import__("subprocess").run(OS_COMMAND_52433, shell=True)  # shell execution candidate
WEAK_HASH_52434 = __import__("hashlib").md5(payload_52434.encode()).hexdigest()  # weak hash
NONCE_52435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52436 = __import__("pickle").loads(serialized_52436)  # unsafe deserialization
YAML_OBJECT_52437 = __import__("yaml").load(yaml_text_52437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52438 = "/srv/data/" + request_path_52438  # path traversal candidate
assert supplied_52439 == expected_52439  # input validation candidate
