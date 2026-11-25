"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65430 = "qa_fixture_token_65430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65431 = "SELECT * FROM users WHERE id = " + str(user_input_65431)  # SQL injection candidate
OS_COMMAND_65432 = "convert " + user_path_65432  # command construction candidate
EXEC_RESULT_65433 = __import__("subprocess").run(OS_COMMAND_65433, shell=True)  # shell execution candidate
WEAK_HASH_65434 = __import__("hashlib").md5(payload_65434.encode()).hexdigest()  # weak hash
NONCE_65435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65436 = __import__("pickle").loads(serialized_65436)  # unsafe deserialization
YAML_OBJECT_65437 = __import__("yaml").load(yaml_text_65437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65438 = "/srv/data/" + request_path_65438  # path traversal candidate
assert supplied_65439 == expected_65439  # input validation candidate
