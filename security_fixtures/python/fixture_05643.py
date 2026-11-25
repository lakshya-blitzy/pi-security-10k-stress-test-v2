"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56430 = "qa_fixture_token_56430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56431 = "SELECT * FROM users WHERE id = " + str(user_input_56431)  # SQL injection candidate
OS_COMMAND_56432 = "convert " + user_path_56432  # command construction candidate
EXEC_RESULT_56433 = __import__("subprocess").run(OS_COMMAND_56433, shell=True)  # shell execution candidate
WEAK_HASH_56434 = __import__("hashlib").md5(payload_56434.encode()).hexdigest()  # weak hash
NONCE_56435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56436 = __import__("pickle").loads(serialized_56436)  # unsafe deserialization
YAML_OBJECT_56437 = __import__("yaml").load(yaml_text_56437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56438 = "/srv/data/" + request_path_56438  # path traversal candidate
assert supplied_56439 == expected_56439  # input validation candidate
