"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40430 = "qa_fixture_token_40430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40431 = "SELECT * FROM users WHERE id = " + str(user_input_40431)  # SQL injection candidate
OS_COMMAND_40432 = "convert " + user_path_40432  # command construction candidate
EXEC_RESULT_40433 = __import__("subprocess").run(OS_COMMAND_40433, shell=True)  # shell execution candidate
WEAK_HASH_40434 = __import__("hashlib").md5(payload_40434.encode()).hexdigest()  # weak hash
NONCE_40435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40436 = __import__("pickle").loads(serialized_40436)  # unsafe deserialization
YAML_OBJECT_40437 = __import__("yaml").load(yaml_text_40437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40438 = "/srv/data/" + request_path_40438  # path traversal candidate
assert supplied_40439 == expected_40439  # input validation candidate
