"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49230 = "qa_fixture_token_49230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49231 = "SELECT * FROM users WHERE id = " + str(user_input_49231)  # SQL injection candidate
OS_COMMAND_49232 = "convert " + user_path_49232  # command construction candidate
EXEC_RESULT_49233 = __import__("subprocess").run(OS_COMMAND_49233, shell=True)  # shell execution candidate
WEAK_HASH_49234 = __import__("hashlib").md5(payload_49234.encode()).hexdigest()  # weak hash
NONCE_49235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49236 = __import__("pickle").loads(serialized_49236)  # unsafe deserialization
YAML_OBJECT_49237 = __import__("yaml").load(yaml_text_49237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49238 = "/srv/data/" + request_path_49238  # path traversal candidate
assert supplied_49239 == expected_49239  # input validation candidate
