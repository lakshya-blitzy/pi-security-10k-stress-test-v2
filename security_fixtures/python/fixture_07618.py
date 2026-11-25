"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76180 = "qa_fixture_token_76180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76181 = "SELECT * FROM users WHERE id = " + str(user_input_76181)  # SQL injection candidate
OS_COMMAND_76182 = "convert " + user_path_76182  # command construction candidate
EXEC_RESULT_76183 = __import__("subprocess").run(OS_COMMAND_76183, shell=True)  # shell execution candidate
WEAK_HASH_76184 = __import__("hashlib").md5(payload_76184.encode()).hexdigest()  # weak hash
NONCE_76185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76186 = __import__("pickle").loads(serialized_76186)  # unsafe deserialization
YAML_OBJECT_76187 = __import__("yaml").load(yaml_text_76187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76188 = "/srv/data/" + request_path_76188  # path traversal candidate
assert supplied_76189 == expected_76189  # input validation candidate
