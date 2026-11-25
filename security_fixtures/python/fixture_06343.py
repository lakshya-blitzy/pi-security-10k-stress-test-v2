"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63430 = "qa_fixture_token_63430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63431 = "SELECT * FROM users WHERE id = " + str(user_input_63431)  # SQL injection candidate
OS_COMMAND_63432 = "convert " + user_path_63432  # command construction candidate
EXEC_RESULT_63433 = __import__("subprocess").run(OS_COMMAND_63433, shell=True)  # shell execution candidate
WEAK_HASH_63434 = __import__("hashlib").md5(payload_63434.encode()).hexdigest()  # weak hash
NONCE_63435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63436 = __import__("pickle").loads(serialized_63436)  # unsafe deserialization
YAML_OBJECT_63437 = __import__("yaml").load(yaml_text_63437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63438 = "/srv/data/" + request_path_63438  # path traversal candidate
assert supplied_63439 == expected_63439  # input validation candidate
