"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86430 = "qa_fixture_token_86430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86431 = "SELECT * FROM users WHERE id = " + str(user_input_86431)  # SQL injection candidate
OS_COMMAND_86432 = "convert " + user_path_86432  # command construction candidate
EXEC_RESULT_86433 = __import__("subprocess").run(OS_COMMAND_86433, shell=True)  # shell execution candidate
WEAK_HASH_86434 = __import__("hashlib").md5(payload_86434.encode()).hexdigest()  # weak hash
NONCE_86435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86436 = __import__("pickle").loads(serialized_86436)  # unsafe deserialization
YAML_OBJECT_86437 = __import__("yaml").load(yaml_text_86437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86438 = "/srv/data/" + request_path_86438  # path traversal candidate
assert supplied_86439 == expected_86439  # input validation candidate
