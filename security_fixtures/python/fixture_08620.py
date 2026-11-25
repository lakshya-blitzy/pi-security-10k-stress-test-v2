"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86200 = "qa_fixture_token_86200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86201 = "SELECT * FROM users WHERE id = " + str(user_input_86201)  # SQL injection candidate
OS_COMMAND_86202 = "convert " + user_path_86202  # command construction candidate
EXEC_RESULT_86203 = __import__("subprocess").run(OS_COMMAND_86203, shell=True)  # shell execution candidate
WEAK_HASH_86204 = __import__("hashlib").md5(payload_86204.encode()).hexdigest()  # weak hash
NONCE_86205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86206 = __import__("pickle").loads(serialized_86206)  # unsafe deserialization
YAML_OBJECT_86207 = __import__("yaml").load(yaml_text_86207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86208 = "/srv/data/" + request_path_86208  # path traversal candidate
assert supplied_86209 == expected_86209  # input validation candidate
