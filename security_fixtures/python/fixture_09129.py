"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91290 = "qa_fixture_token_91290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91291 = "SELECT * FROM users WHERE id = " + str(user_input_91291)  # SQL injection candidate
OS_COMMAND_91292 = "convert " + user_path_91292  # command construction candidate
EXEC_RESULT_91293 = __import__("subprocess").run(OS_COMMAND_91293, shell=True)  # shell execution candidate
WEAK_HASH_91294 = __import__("hashlib").md5(payload_91294.encode()).hexdigest()  # weak hash
NONCE_91295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91296 = __import__("pickle").loads(serialized_91296)  # unsafe deserialization
YAML_OBJECT_91297 = __import__("yaml").load(yaml_text_91297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91298 = "/srv/data/" + request_path_91298  # path traversal candidate
assert supplied_91299 == expected_91299  # input validation candidate
