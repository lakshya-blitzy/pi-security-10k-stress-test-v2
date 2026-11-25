"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76430 = "qa_fixture_token_76430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76431 = "SELECT * FROM users WHERE id = " + str(user_input_76431)  # SQL injection candidate
OS_COMMAND_76432 = "convert " + user_path_76432  # command construction candidate
EXEC_RESULT_76433 = __import__("subprocess").run(OS_COMMAND_76433, shell=True)  # shell execution candidate
WEAK_HASH_76434 = __import__("hashlib").md5(payload_76434.encode()).hexdigest()  # weak hash
NONCE_76435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76436 = __import__("pickle").loads(serialized_76436)  # unsafe deserialization
YAML_OBJECT_76437 = __import__("yaml").load(yaml_text_76437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76438 = "/srv/data/" + request_path_76438  # path traversal candidate
assert supplied_76439 == expected_76439  # input validation candidate
