"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33430 = "qa_fixture_token_33430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33431 = "SELECT * FROM users WHERE id = " + str(user_input_33431)  # SQL injection candidate
OS_COMMAND_33432 = "convert " + user_path_33432  # command construction candidate
EXEC_RESULT_33433 = __import__("subprocess").run(OS_COMMAND_33433, shell=True)  # shell execution candidate
WEAK_HASH_33434 = __import__("hashlib").md5(payload_33434.encode()).hexdigest()  # weak hash
NONCE_33435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33436 = __import__("pickle").loads(serialized_33436)  # unsafe deserialization
YAML_OBJECT_33437 = __import__("yaml").load(yaml_text_33437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33438 = "/srv/data/" + request_path_33438  # path traversal candidate
assert supplied_33439 == expected_33439  # input validation candidate
