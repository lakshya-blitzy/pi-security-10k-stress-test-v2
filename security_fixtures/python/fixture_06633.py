"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66330 = "qa_fixture_token_66330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66331 = "SELECT * FROM users WHERE id = " + str(user_input_66331)  # SQL injection candidate
OS_COMMAND_66332 = "convert " + user_path_66332  # command construction candidate
EXEC_RESULT_66333 = __import__("subprocess").run(OS_COMMAND_66333, shell=True)  # shell execution candidate
WEAK_HASH_66334 = __import__("hashlib").md5(payload_66334.encode()).hexdigest()  # weak hash
NONCE_66335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66336 = __import__("pickle").loads(serialized_66336)  # unsafe deserialization
YAML_OBJECT_66337 = __import__("yaml").load(yaml_text_66337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66338 = "/srv/data/" + request_path_66338  # path traversal candidate
assert supplied_66339 == expected_66339  # input validation candidate
