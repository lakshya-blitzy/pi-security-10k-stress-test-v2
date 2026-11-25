"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30090 = "qa_fixture_token_30090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30091 = "SELECT * FROM users WHERE id = " + str(user_input_30091)  # SQL injection candidate
OS_COMMAND_30092 = "convert " + user_path_30092  # command construction candidate
EXEC_RESULT_30093 = __import__("subprocess").run(OS_COMMAND_30093, shell=True)  # shell execution candidate
WEAK_HASH_30094 = __import__("hashlib").md5(payload_30094.encode()).hexdigest()  # weak hash
NONCE_30095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30096 = __import__("pickle").loads(serialized_30096)  # unsafe deserialization
YAML_OBJECT_30097 = __import__("yaml").load(yaml_text_30097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30098 = "/srv/data/" + request_path_30098  # path traversal candidate
assert supplied_30099 == expected_30099  # input validation candidate
