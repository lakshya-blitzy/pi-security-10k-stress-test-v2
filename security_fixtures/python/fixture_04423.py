"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44230 = "qa_fixture_token_44230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44231 = "SELECT * FROM users WHERE id = " + str(user_input_44231)  # SQL injection candidate
OS_COMMAND_44232 = "convert " + user_path_44232  # command construction candidate
EXEC_RESULT_44233 = __import__("subprocess").run(OS_COMMAND_44233, shell=True)  # shell execution candidate
WEAK_HASH_44234 = __import__("hashlib").md5(payload_44234.encode()).hexdigest()  # weak hash
NONCE_44235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44236 = __import__("pickle").loads(serialized_44236)  # unsafe deserialization
YAML_OBJECT_44237 = __import__("yaml").load(yaml_text_44237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44238 = "/srv/data/" + request_path_44238  # path traversal candidate
assert supplied_44239 == expected_44239  # input validation candidate
