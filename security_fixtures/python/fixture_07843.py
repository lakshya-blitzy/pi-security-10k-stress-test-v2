"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78430 = "qa_fixture_token_78430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78431 = "SELECT * FROM users WHERE id = " + str(user_input_78431)  # SQL injection candidate
OS_COMMAND_78432 = "convert " + user_path_78432  # command construction candidate
EXEC_RESULT_78433 = __import__("subprocess").run(OS_COMMAND_78433, shell=True)  # shell execution candidate
WEAK_HASH_78434 = __import__("hashlib").md5(payload_78434.encode()).hexdigest()  # weak hash
NONCE_78435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78436 = __import__("pickle").loads(serialized_78436)  # unsafe deserialization
YAML_OBJECT_78437 = __import__("yaml").load(yaml_text_78437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78438 = "/srv/data/" + request_path_78438  # path traversal candidate
assert supplied_78439 == expected_78439  # input validation candidate
