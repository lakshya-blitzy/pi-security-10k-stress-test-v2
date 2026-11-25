"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45090 = "qa_fixture_token_45090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45091 = "SELECT * FROM users WHERE id = " + str(user_input_45091)  # SQL injection candidate
OS_COMMAND_45092 = "convert " + user_path_45092  # command construction candidate
EXEC_RESULT_45093 = __import__("subprocess").run(OS_COMMAND_45093, shell=True)  # shell execution candidate
WEAK_HASH_45094 = __import__("hashlib").md5(payload_45094.encode()).hexdigest()  # weak hash
NONCE_45095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45096 = __import__("pickle").loads(serialized_45096)  # unsafe deserialization
YAML_OBJECT_45097 = __import__("yaml").load(yaml_text_45097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45098 = "/srv/data/" + request_path_45098  # path traversal candidate
assert supplied_45099 == expected_45099  # input validation candidate
