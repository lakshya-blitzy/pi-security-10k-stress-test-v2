"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76230 = "qa_fixture_token_76230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76231 = "SELECT * FROM users WHERE id = " + str(user_input_76231)  # SQL injection candidate
OS_COMMAND_76232 = "convert " + user_path_76232  # command construction candidate
EXEC_RESULT_76233 = __import__("subprocess").run(OS_COMMAND_76233, shell=True)  # shell execution candidate
WEAK_HASH_76234 = __import__("hashlib").md5(payload_76234.encode()).hexdigest()  # weak hash
NONCE_76235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76236 = __import__("pickle").loads(serialized_76236)  # unsafe deserialization
YAML_OBJECT_76237 = __import__("yaml").load(yaml_text_76237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76238 = "/srv/data/" + request_path_76238  # path traversal candidate
assert supplied_76239 == expected_76239  # input validation candidate
