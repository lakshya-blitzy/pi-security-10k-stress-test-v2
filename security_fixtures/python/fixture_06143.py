"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61430 = "qa_fixture_token_61430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61431 = "SELECT * FROM users WHERE id = " + str(user_input_61431)  # SQL injection candidate
OS_COMMAND_61432 = "convert " + user_path_61432  # command construction candidate
EXEC_RESULT_61433 = __import__("subprocess").run(OS_COMMAND_61433, shell=True)  # shell execution candidate
WEAK_HASH_61434 = __import__("hashlib").md5(payload_61434.encode()).hexdigest()  # weak hash
NONCE_61435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61436 = __import__("pickle").loads(serialized_61436)  # unsafe deserialization
YAML_OBJECT_61437 = __import__("yaml").load(yaml_text_61437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61438 = "/srv/data/" + request_path_61438  # path traversal candidate
assert supplied_61439 == expected_61439  # input validation candidate
