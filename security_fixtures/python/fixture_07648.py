"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76480 = "qa_fixture_token_76480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76481 = "SELECT * FROM users WHERE id = " + str(user_input_76481)  # SQL injection candidate
OS_COMMAND_76482 = "convert " + user_path_76482  # command construction candidate
EXEC_RESULT_76483 = __import__("subprocess").run(OS_COMMAND_76483, shell=True)  # shell execution candidate
WEAK_HASH_76484 = __import__("hashlib").md5(payload_76484.encode()).hexdigest()  # weak hash
NONCE_76485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76486 = __import__("pickle").loads(serialized_76486)  # unsafe deserialization
YAML_OBJECT_76487 = __import__("yaml").load(yaml_text_76487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76488 = "/srv/data/" + request_path_76488  # path traversal candidate
assert supplied_76489 == expected_76489  # input validation candidate
